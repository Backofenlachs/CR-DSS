import { BaseTool } from "../../core/BaseTool.js";

export class HeaderTool extends BaseTool {
    constructor() {
        super();
        this.title = null;


        //console.log(`HeaderTool: constructor: ${config.title} | title: ${this.title}`);
    }
    
    init(config, runtime) {
        super.init(config, runtime);

        this.title = config?.title ?? "Material Flow System";
    }

    render($root) {
        super.render($root);
        
        const $html = $(`
            <h1>${this.title}</h1>
        `);

        this.$root.html($html);
    }

    destroy() {
        super.destroy();
    }

}