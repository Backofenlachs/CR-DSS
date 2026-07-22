import {
    AppController,
    SlotNames,
    slot
} from "../../libs/ui-engine-v0_2_0/index.js";
import type { LayoutConfig } from "../../libs/ui-engine-v0_2_0/index.js";

import  { CRDSSHeaderTool } from "./tools/CRDSSHeaderTool.js"
import type { CRDSSHeaderConfig } from "./tools/CRDSSHeaderTool.js";


const HEADER_CONFIG: CRDSSHeaderConfig = {
    title: "CR-DSS",
    subtitle: "Credit Risk Decision Support System",

    versions: {
        riskEngine: "0.2.0",
        server: "0.1.0",
        ui: "0.1.0"
    }
};

const LAYOUT_CONFIG = {
    layout: slot(
        "div",
        SlotNames.HEADER,
    ),

    mounts: [
        {
            slotName: SlotNames.HEADER,
            toolName: "cr-dss-header",
            toolClass: CRDSSHeaderTool,
            config: HEADER_CONFIG,
            activeOnLoad: true
        }
    ]
} satisfies LayoutConfig;

document.addEventListener("DOMContentLoaded", () => {
    const $app = $("#app");

    const appController = new AppController();
    appController.init(
        $app,
        LAYOUT_CONFIG
    );
});