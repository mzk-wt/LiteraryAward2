/**
 * サイドバーコンポーネント
 */
Vue.component('sidebar1', {
    props: ['rootpath'],
    template: `
        <div>
            <div class="box">
                <div class="mb-2"><button class="button is-info is-light is-fullwidth" @click="showAwardList">文学賞から探す</button></div>
                <div class="mb-2"><button class="button is-info is-light is-fullwidth" @click="showAuthorList">著者から探す</button></div>
                <div class="mb-2"><button class="button is-info is-light is-fullwidth" @click="showBookList">書籍から探す</button></div>
            </div>
        </div>
    `,
    methods: {
        showAwardList: function() {
            document.location.href = this.rootpath + "pages/list.htm?list=award";
        },
        showAuthorList: function() {
            document.location.href = this.rootpath + "pages/list.htm?list=author";
        },
        showBookList: function() {
            document.location.href = this.rootpath + "pages/list.htm?list=book";
        }
    }
});