/**
 * 一覧コンポーネント
 */
Vue.component('list', {
    props: ['listtype', 'listkey', 'rootpath'],
    template: `
        <div>
            <table class="table is-bordered is-striped is-hoverable is-fullwidth is-size-7">
                <tr>
                    <th v-for="title in listtitle" :key="title">{{ title }}</th>
                </tr>
                <tr v-for="item in listitem" :key="item.key">
                    <td v-for="(v, i) in item.value" :key="i" :class="v.class" v-html="v.text"></td>
                </tr>
            </table>
        </div>
    `,
    data() {
        return {
            listtitle: [],
            listitem: []
        }
    },
    created() {
        // JSONデータから一覧に表示する項目を取得する
        axios.get(this.rootpath + "json/" + this.listtype + ".json").then(s => {
            let d = s.data;
            if (this.listkey) {
                d = s.data[this.listkey];
            }

            this.listtitle = d.listtitle;
            this.listitem = d.listitem;
        });
    },
});