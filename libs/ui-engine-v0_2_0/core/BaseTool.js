/**
 * Abstract base class for all mountable tools.
 * 
 * A Tool is a self-contained UI module mounted into a slot provided by the AppShell.
 * 
 * The AppController and MountingEngine coordinate which tools are mounted into wich
 * slots.
 * 
 * BaseTool defines the standardized lifecycle:
 * 
 * constructor() -> init(config, runtime) -> render($root) -> destroy()
 *
 * Concrete tools may:
 * - implement lightweight UI logic directly
 * - or act as adapters for internal MVC/controller structure
 *  
 * Responsibilities:
 * - receive tool configuration and runtime references
 * - render only inside the assigned root container
 * - cleanup internal state and DOM bindings on destroy
 * 
 * @abstract
 */
export class BaseTool {

    constructor() {
        if (new.target === BaseTool) {
            throw new Error("BaseTool darf nicht direkt instanziiert werden.");
        }
        
        // Internal lifecycle state
        this.initialized = false;
        this.rendered = false;

        // shared runtime references
        this.config = null;
        this.runtime = null;

        // DOM references
        this.$root = null;
    }

    /**
     * Initialize the tool state and runtime references.
     * 
     * @param {Object} [config={}]
     * @param {Object} [runtime={}]
     * @returns {void}
    */
    init(config={}, runtime={}) {
        this.config = config;
        this.runtime = runtime;

        this.initialized = true;
    }

    /**
     * Render the tool inside the assigned root container.
     *
     * @param {jQuery}
     * @returns {void}
     */
    render($root) {
        if (!$root || !$root.jquery || $root.length === 0) {
            throw new Error(
                "[BaseTool.render] Invalid $root: expected non-empty jQuery object"
            );
        }

        this.$root = $root;

        this.rendered = true;
    }

    /**
     * Cleanup hook called before unmounting the tool.
     * 
     * @returns {void}
     */
    destroy() {
        if (this.$root) {
            this.$root.empty();
        }

        this.$root = null;
        this.rendered = false;
        this.initialized = false;
    }

    getStatus() {
        return {
            initialized: this.initialized,
            rendered: this.rendered,
            hasRoot: !!this.$root
        }
    }
}