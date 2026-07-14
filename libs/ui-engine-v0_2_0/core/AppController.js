// core
import { MountingEngine } from "./MountingEngine.js";
import { AppShell } from "./AppShell.js";


export class AppController {
    constructor() {
        this.appShell = null
        this.mountingEngine = null;
        this.layoutConfig = null;
        this.runtime = null;

        // states
        this.initialized = false;
    }

    init($rootElement , layoutConfig) {
        this.isJqueryLoaded();

        // validating $rootElement as JQuery object
        if (!$rootElement || !$rootElement.jquery || $rootElement.length === 0) {
            throw new Error(
                "[AppController] Invalid root element: expected jQuery object"
            );
        }

        // checking layoutConfig is set properly
        this.validateLayoutConfig(layoutConfig);
        
        // only one init per AppController possible.
        if (this.initialized) {
            throw new Error(
                "[AppController] Already initialized"
            );
        }

        // INTANZIATE core components
        this.layoutConfig = layoutConfig;
        this.appShell = new AppShell();
        this.mountingEngine = new MountingEngine();

        // CREATE runtime environment
        this.runtime = this.createRuntime();

        // INITIALISE and connect core Componentns 
        this.appShell.init($rootElement, this.layoutConfig.layout);
        this.mountingEngine.init(this.appShell, this.runtime);        
        
        // register everytool tool from appShell.mounts in toolRegestry
        this.layoutConfig.mounts.forEach((tool) => {
            this.mountingEngine.registerTool(tool.toolName, tool.toolClass);
            
        });

        // mount all aktive tools based on layoutConfig actieveOnload=true
        this.layoutConfig.mounts.forEach((tool) =>  {
            if (!tool.activeOnLoad) {
                return
            }

            console.log("config:", tool.config);
            this.mountingEngine.mountTool(tool.toolName, tool.slotName, tool.config);

        });

        this.initialized = true;
    }

    destroy(){
        this.mountingEngine.destroy();
        this.appShell.destroy();
        
        this.layoutConfig = null;
        this.mountingEngine = null;
        this.appShell = null;
    }

    validateLayoutConfig(layoutConfig) {
        if(!layoutConfig || typeof layoutConfig !== "object") {
            throw new Error(
                "[AppController] layoutConfig must be an object"
            );
        }

        if(!layoutConfig.layout || typeof layoutConfig.layout !== "object") {
            throw new Error(
                "[AppController] layoutConfig: layoutConfig.layout must be an object"
            );
        }

        if(!Array.isArray(layoutConfig.mounts)) {
            throw new Error(
                "[AppController] layoutConfig.mounts must be an array"
            );
        }
    }

    createRuntime()
    {
        return {
            mountingEngine: this.mountingEngine
        };
    }

    isJqueryLoaded() {
        if (
            typeof window.jQuery !== "function" ||
            !window.jQuery.fn
        ) {
            throw new Error(
                "[AppController.init] Valid jQuery instance not found."
            );
        }
    }
}