/**
 * フッターコンポーネント
 */
 Vue.component('footer1', {
    props: ['rootpath'],
    template: `
        <footer class="footer">
            <div class="content has-text-centered">
                <p>
                    <a href="https://store.line.me/stickershop/author/5892638/ja" target="_blank">
                        <img :src="rootpath + 'img/neko_borg_banner_main.jpg'" style="width:512px;" />
                    </a>
                </p>
            </div>
            <div class="content has-text-centered">
                <p>
                    &copy; 2020 LADB
                    &nbsp;&nbsp;
                    <a href="https://twitter.com/LiteraryAwardDB" target="_blank">
                        <img :src="rootpath + 'img/Twitter_Social_Icon_Circle_Color.png'" style="width:30px; vertical-align:middle;">
                    </a>
                </p>
            </div>
        </footer>
    `
});
