# UI-Engine v0.2.0

Release snapshot of the UI-Engine.

Contains:
- core runtime
- layout factory
- slot system
- standard tools
- base styling
- local jQuery dependency

Does not contain:
- example tools
- documentation
- architecture sketches
- ADRs
- demo layouts

Full documentation:
https://github.com/BackofenLachs/UI-Engine

## Minimal Setup

### index.html
```HTML
<link rel="stylesheet" href="./ui-engine-v0_2_0/styles/main.css">

<script src="./ui-engine-v0_2_0/lib/jquery-4.0.0.min.js"></script>
<script src="./app.js" type="module"></script>

<div id="app"></div>
```

### app.js
```JS
import {
    AppController,
    slot,
    SlotNames,
    HeaderTool
} from "./ui-engine-v0_2_0/index.js";


const layoutConfig = {
    layout: slot('div', SlotNames.HEADER, ["wireframe"]),
    mounts: [
        {// HeaderTool in HEADER slot
            slotName: SlotNames.HEADER,
            toolName: "header",
            toolClass: HeaderTool,
            config: null,
            activeOnLoad: true
        }
    ]
}

$(document).ready(() => {
    const $app = $("#app");
    
    const appController = new AppController();
    appController.init($app, layoutConfig);

});
```

---

### Result

```
Custom layout
    -> initalize AppController
        -> mount tools dynamically
```