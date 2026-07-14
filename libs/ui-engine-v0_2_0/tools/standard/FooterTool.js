import { BaseTool } from "../../core/BaseTool.js";


export class FooterTool extends BaseTool {
    constructor() {
        super();

        this.text = null;
    }  

    init(config, runtime) {
        super.init(config, runtime);
        
        this.text = config?.text ?? "© 2026 Material Flow System. All rights reserved. ";
    }
    
    render($root) {
        super.render($root);

        const $html = $(`
            <p>${this.text}</p>
        `);

        this.$root.html($html);
    }

    destroy() {
        super.destroy();
    }
}