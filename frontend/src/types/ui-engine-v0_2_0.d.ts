// frontend/src/types/ui-engine-v0_2_0.d.ts

interface UiEngineRoot {
    readonly jquery: string;
    readonly length: number;
    
    html(contend: string | UiEngineRoot): UiEngineRoot;
    empty(): UiEngineRoot;
}

declare function $(selector: string): UiEngineRoot;

declare module "*ui-engine-v0_2_0/index.js" {
    export type LayoutNode = {
        tag: string;
        classes: string[];
        children: LayoutNode[];

        slot?: string;
        style: unknown[] | null;
    };
    
    export function slot(
        tag: string,
        slotName: string,
        classes?: string[]
    ): LayoutNode;

    export function node(
        tag?: string,
        classes?: string[],
        children?: LayoutNode[],
        style?: unknown[] | null
    ): LayoutNode;


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