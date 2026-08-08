import {
    AppController,
    SlotNames,
    node,
    slot
} from "../../libs/ui-engine-v0_2_0/index.js";
import type { LayoutConfig } from "../../libs/ui-engine-v0_2_0/index.js";

import { HEADER_CONFIG } from "./config/applicationConfig.js";

import  { CRDSSHeaderTool, type CRDSSHeaderConfig } from "./tools/CRDSSHeaderTool.js"
import { ApplicantRequestTool } from "./tools/ApplicantRequestTool.js";
import { RiskResultTool } from "./tools/RiskResultTool.js";

const CRDSS_SLOT_NAMES = {
    APPLICANT_REQUEST: "applicant-request",
    RISK_ASSESMENT: "risk-assessment"
} as const;

const LAYOUT_CONFIG = {
    layout: node("div", ["crdss-shell"], [
        slot("div", SlotNames.HEADER,),
        node("main", ["crdss-workspace"],[
            slot("div", CRDSS_SLOT_NAMES.APPLICANT_REQUEST, ["crdss-workspace__request"]),
            slot("div", CRDSS_SLOT_NAMES.RISK_ASSESMENT, ["crdss-workspace__result"])
        ])
    ]),
    mounts: [
        { // HEADER 
            slotName: SlotNames.HEADER,
            toolName: "cr-dss-header",
            toolClass: CRDSSHeaderTool,
            config: HEADER_CONFIG,
            activeOnLoad: true
        },
        { // APPLICANT REQUEST
            slotName: CRDSS_SLOT_NAMES.APPLICANT_REQUEST,
            toolName: "applicant-request",
            toolClass: ApplicantRequestTool,
            config: null,
            activeOnLoad: true
        }, 
        { // RISK RESULT
            slotName: CRDSS_SLOT_NAMES.RISK_ASSESMENT,
            toolName: "risk-result",
            toolClass: RiskResultTool,
            config: null,
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