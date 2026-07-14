import {
    AppController,
    slot,
    SlotNames,
    HeaderTool
} from "./../libs/ui-engine-v0_2_0/index.js";


const layoutConfig = {
    layout: slot('div', SlotNames.HEADER, ["wireframe"]),
    mounts: [
        {// HeaderTool in HEADER slot
            slotName: SlotNames.HEADER,
            toolName: "header",
            toolClass: HeaderTool,
            config: {title: "Credit Risk – Decision Support System"},
            activeOnLoad: true
        }
    ]
}

$(document).ready(() => {
    const $app = $("#app");
    
    const appController = new AppController();
    appController.init($app, layoutConfig);

});