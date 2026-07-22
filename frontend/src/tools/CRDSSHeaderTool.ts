import { BaseTool } from "../../../libs/ui-engine-v0_2_0/index.js"

export interface CRDSSHeaderConfig {
    title: string;
    subtitle: string;

    versions: {
        riskEngine: string;
        server: string;
        ui: string;
    }
}


const DEFAULT_CONFIG: CRDSSHeaderConfig = {
    title: "CR-DSS",
    subtitle: "Credit Risk Decision Support System",

    versions: {
        riskEngine: "0.2.0",
        server: "0.1.0",
        ui: "0.1.0"
    }
};

export class CRDSSHeaderTool extends BaseTool {
    private headerConfig: CRDSSHeaderConfig = DEFAULT_CONFIG;

    override init(
        config: unknown = {},
        runtime: unknown = {}
    ): void  {
        super.init(config, runtime);

        const suppliedConfig = (config ?? {}) as Partial<CRDSSHeaderConfig>;

        this.headerConfig = {
            title: suppliedConfig.title ?? DEFAULT_CONFIG.title,
            subtitle: suppliedConfig.subtitle ?? DEFAULT_CONFIG.subtitle,
            versions: {
                ...DEFAULT_CONFIG.versions,
                ...suppliedConfig.versions
            }
        }
    }

    override render($root: UiEngineRoot): void {
        super.render($root);

        const {
            title, 
            subtitle,
            versions
        } = this.headerConfig;

        const $header = $(/*html*/`
            <header class="crdss-header">
                <div class="crdss-header__identity">
                    <div class="crdss-header__logo" aria-hidden="true">CR</div>
                    <div class="crdss-header__product">
                        <div class=crdss-header__title>${title}</div>
                        <div class=crdss-header__subtitle>${subtitle}</div>
                    </div>
                </div>
                <div class="crdss-header__versions" aria-label="Application versions">
                    <span>Risk Engine ${versions.riskEngine}</span>
                    <span>Server ${versions.server}</span>
                    <span>UI ${versions.ui} </span>
                </div>
            </header>
        `);

        $root.html($header)
    }
}