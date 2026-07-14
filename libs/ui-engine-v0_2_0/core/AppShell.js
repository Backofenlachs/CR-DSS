/**
 * AppShell
 * 
 * Responsible for rendering the application layout from a configuration object 
 * and managing named slot regions within the DOM.
 * 
 * Core responsibilities:
 * - Translates a layout configuration (tree structure) into DOM elements
 * - Identifies and chaches all slots elements (data-slots)
 * - Provides access to slots for external systems (e.g. MountingEngine)
 * 
 * Notes:
 * - Does not handle any business logic or tool rendering
 * - Acts as the stuctural foundation for the UI
 * 
 * important:
 * - The 'data-slot' attribute in the DOM acts as the unique key for slot identification and access
 */

export class AppShell {
    constructor($rootElement) {
        this.dom = {
            root: null,
            slots: {}
        };
    }

    init($rootAppElement, layoutConfig) {
        this.dom.root = $rootAppElement;

        const html = this.renderNode(layoutConfig);
        this.dom.root.html(html);
        this.cacheSlots();
    }


    /**
     * Recursively renders a layout node and its children into an HTML string.
     *
     * Notes:
     * - Uses the layout configuration tree as input
     * - Supports nested child nodes
     * - Adds slot metadata via the 'data-slot' attribute when configured
     */
    renderNode(nodeConfig) {
        const {
            // node optionen
            tag = "div",
            slot = null,
            //id = "",
            style = [],
            classes = [],
            children = []
        } = nodeConfig;

        const classAttr = classes.length ? `class="${classes.join(" ")}"` : "";
        //const idAttr = id ? `id="${id}"` : null;
        const slotAttr = slot ? `data-slot="${slot}"` : "";
        const styleAttr = style ? `style="${style.join(";")}"`: "";
        
        const childrenHtml = children.map(child => this.renderNode(child)).join("");

        return `
            <${tag} ${classAttr} ${slotAttr} ${styleAttr}>
                ${childrenHtml}
            </${tag}>
        `;
    }

    /**
     * caches htmlElements by 'data-slot'
     */
    cacheSlots() {
        this.dom.root.find("[data-slot]").each((index, element) => {
            const $element = $(element);
            const slotName = $element.data("slot");
            this.dom.slots[slotName] = $element;
        });

        console.log("AppShell: cached slots", this.dom.slots);
    }

    getSlot(slotName) {
        return this.dom.slots[slotName] || null;
    }
}