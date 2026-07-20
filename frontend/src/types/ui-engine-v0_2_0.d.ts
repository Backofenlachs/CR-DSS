// frontend/src/types/ui-engine-v0_2_0.d.ts

interface UiEngineRoot {
    readonly length: number;
}

declare function $(selector: string): UiEngineRoot;

declare module "*ui-engine-v0_2_0/index.js" {
    export type LayoutNode = unknown;

    export type ToolConstructor = new () => object;

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

    export class HeaderTool {
        constructor();
    }

    export class AppController {
        constructor();

        init(
            root: UiEngineRoot,
            layoutConfig: LayoutConfig
        ): void;

        destroy(): void;
    }
}