// frontend/src/types/ui-engine-v0_2_0.d.ts

interface UiEngineRoot {
    readonly jquery: string;
    readonly length: number;
    
    html(contend: string | UiEngineRoot): UiEngineRoot;
    empty(): UiEngineRoot;
}

declare function $(selector: string): UiEngineRoot;

declare module "*ui-engine-v0_2_0/index.js" {
    export type LayoutNode = unknown;

    export abstract class BaseTool {
        constructor();

        init(
            config?: unknown,
            runtime?: unknown
        ): void;

        render($root: UiEngineRoot): void;

        destroy(): void;

        getStatus(): {
            initialized: boolean;
            rendered: boolean;
            hasRoot: boolean;
        }
    }

    export type ToolConstructor = new () => BaseTool;

    export interface MountDefinition {
        slotName: string;
        toolName: string;
        toolClass: ToolConstructor;
        config: unknown;
        activeOnLoad: boolean;
    }

    export interface LayoutConfig {
        layout: LayoutNode;
        mounts: MountDefinition[];
    }

    export const SlotNames: Readonly<Record<string, string>> & {
        readonly HEADER: string;
    };

    export function slot(
        elementName: string,
        slotName: string,
        classNames?: readonly string[]
    ): LayoutNode;

    export class HeaderTool extends BaseTool  {}

    export class AppController {
        constructor();

        init(
            root: UiEngineRoot,
            layoutConfig: LayoutConfig
        ): void;

        destroy(): void;
    }
}