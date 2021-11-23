/*
 * パンくずリストコンポーネント
 */
 Vue.component('breadcrumb', {
    props: ['rootpath', 'linkkeys'],
    template: `
        <nav class="breadcrumb is-size-7" aria-label="breadcrumbs">
            <ul>
                <template v-for="(link, index) in links">
                    <li v-if="index < links.length - 1" :key="link.no"><a :href="link.url">{{ link.text }}</a></li>
                    <li v-else class="is-active" :key="link.no"><a :href="link.url" aria-current="page">{{ link.text }}</a></li>
                </template>
            </ul>
        </nav>
    `,
    data() {
        return {
            links: [] 
        }
    },
    watch: {
        linkkeys(value) {
            this.links = [];
            for (let key of value.split(",")) {
                this.links.push(getPageInfo(this.rootpath, key));
            }
        }
    }
});