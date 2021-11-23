/**
 * フッターコンポーネント
 */
 Vue.component('footer1', {
    props: ['rootpath'],
    template: `
        <footer class="footer">
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