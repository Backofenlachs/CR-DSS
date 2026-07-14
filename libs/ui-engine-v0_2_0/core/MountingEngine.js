/**
 * Mounting (Formerly AppManager)
 * 
 * Central coordinator for tool registration, mounting, unmounting 
 * and switching within appshell slots.
 * 
 * Core responsibilities:
 * - Stores available tool classes in a registry
 * - Instantiates tools fr a given slot
 * - Controls the tool lifecycle (init, render, destroy)
 * - Tracks currently mounted tool instances per slot
 */

import { BaseTool } from "./BaseTool.js";

export class MountingEngine {
    constructor() {
        this.appShell = null;
        this.runtime = null;

        this.toolRegistry = null; // toolName => ToolClass; holds all tools and its definitons that exists in the app
        this.toolInstances = null; // toolName => Tool Instance; For persistence while multiple mounting
        this.mountedTools = null; // slot => toolName
    }

    init(appShell, runtime) {
        this.appShell = appShell;
        this.runtime = runtime;

        this.toolRegistry = new Map();
        this.toolInstances = new Map();
        this.mountedTools = new Map();
    }

    /**
     * Registers a Tool inside the internal tool  regestry.
     * 
     * The regestry stores:
     * key   = toolname
     * value = ToolClass
     * 
     * Every registered ToolClass must inherit from BaseTool.
     * 
     * This method only registers the tool definition.
     * No tool instance will be created.
     */
    registerTool(toolName, ToolClass) {
        if (!toolName || !ToolClass) { 
            throw new Error(
                "[MountingEngine] registerTool(): needs toolName and ToolClass"
            );
        }

        if ( !(ToolClass.prototype instanceof BaseTool) ) { // check if ToolClass extends BaseTool
            throw new Error(
                `[MountingEngine] registerTool(): ToolClass for "${toolName}" has to inherit from BaseTool`
            )
        }

        this.toolRegistry.set(toolName, ToolClass);
    }

    /**
     * - if noInstance, then Creates new Instance in this.toolInstances based on toolRegistry
     * - mounts a registered tool into a slot.
     */
    mountTool(toolName, slotName, config=null) {
        const $slot = this.appShell.getSlot(slotName);
        
        // validate params
        if (!this.toolRegistry.get(toolName)) {
            throw new Error(
                `[MountingEngine] Tool: "${toolName}" is not registered`
            );
        }

        if (!$slot) {
            throw new Error (
                `[MountingEngine] Slot "${slotName} does not exists`
            );
        }

        let toolInstance = null;

        // instaziate tool when no instance in toolInstances exists
        if (!this.toolInstances.get(toolName)) {
            const toolClass = this.toolRegistry.get(toolName);

            this.toolInstances.set(toolName, new toolClass());
            toolInstance = this.toolInstances.get(toolName);

            toolInstance.init(config, this.runtime);
        } else {
            toolInstance =  this.toolInstances.get(toolName); 
        }
        
        if (typeof toolInstance.render === "function") {
            toolInstance.render($slot);
        } else { throw new Error(`[MountingEngine.mountTool] render in toolInstance: ${toolInstance} not implementet`)}

        // add to mountedTool map
        this.mountedTools.set(slotName, toolName);
        
        console.log(`successfully mounted:${toolName}, ${toolInstance}`);
        return toolInstance;
    }

    unmountTool(slotName) {
        const toolName = this.mountedTools.get(slotName);
        if (!toolName) return;

        const instance = this.toolInstances.get(toolName);
        const $slot = this.appShell.getSlot(slotName);

        if ($slot) {
            $slot.empty();
        }
        this.mountedTools.delete(slotName);
    }

    destroyTool(toolName) {
        this.mountedTools.delete(toolName);
        this.toolInstances.get(toolName).destroy();
        this.toolInstances.delete(toolName);
    }

    destroy() {
        // unmount all mounted tools
        for (const slotName of Array.from(this.mountedTools.keys())) {
            this.unmountTool(slotName);
        }

        // destroy all tool instances
        for (const toolName of Array.from(this.toolInstances.keys())) { 
            this.destroyTool(toolName)
        }

        // cleanup all runtime maps
        this.mountedTools.clear();
        this.toolInstances.clear();
        this.toolRegistry.clear();

        this.toolRegistry = null;
        this.toolInstances = null;
        this.mountedTools = null;

        this.appShell = null;
    }

    switchTool(slotName, toolName, config=null) {
        this.unmountTool(slotName);
        return this.mountTool(toolName, slotName, config);
    }

    getMountedToolInstanceBySlotName(slotName) {
        const toolName = this.mountedTools.get(slotName);

        if(toolName == null) {
            return null;
        }
        return this.toolInstances.get(toolName) ?? null;
    }
}