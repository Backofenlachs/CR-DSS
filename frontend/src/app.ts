import {
    AppController,
    HeaderTool,
    SlotNames,
    slot
} from "../../libs/ui-engine-v0_2_0/index.js";

import type {
    LayoutConfig
} from "../../libs/ui-engine-v0_2_0/index.js";

const LAYOUT_CONFIG = {
    layout: slot(
        "div",
        SlotNames.HEADER,
        ["wireframe"]
    ),

    mounts: [
        {
            slotName: SlotNames.HEADER,
            toolName: "header",
            toolClass: HeaderTool,
            config: {
                title: "Credit Risk – Decision Support System"
            },
            activeOnLoad: true
        }
    ]
} satisfies LayoutConfig;

document.addEventListener("DOMContentLoaded", () => {
    const $app = $("#app");

    const appController = new AppController();
    appController.init($app, LAYOUT_CONFIG);
});