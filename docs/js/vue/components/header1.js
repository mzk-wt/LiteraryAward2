/**
 * ヘッダーコンポーネント
 */
Vue.component('header1', {
    props: ['title', 'subtitle', 'rootpath'],
    template: `
        <header class="hero is-light">

            <div class="hero-head">
                <nav class="navbar">
                    <div class="container">
                        <div class="navbar-brand">
                            <a class="navbar-item" :href="rootpath + 'index.htm'">
                                <img :src="rootpath + 'img/Logo.png'">
                            </a>
                            <span class="navbar-burger" data-target="navbarMenuHeroA">
                                <span></span>
                                <span></span>
                                <span></span>
                            </span>
                        </div>
                        <div id="navbarMenuHeroA" class="navbar-menu is-size-7">
                            <div class="navbar-end">
                                <a class="navbar-item" :href="rootpath + 'index.htm'">
                                    <span class="icon"><i class="fas fa-home"></i></span>
                                    <span>Home</span>
                                </a>
                                <a class="navbar-item" :href="rootpath + 'pages/calendar.htm'">
                                    <span class="icon"><i class="far fa-calendar-alt"></i></span>
                                    <span>文学賞カレンダー</span>
                                </a>
                                <a class="navbar-item" :href="rootpath + 'pages/list.htm?list=award'">
                                    <span class="icon"><i class="fas fa-award"></i></span>
                                    <span>文学賞一覧</span>
                                </a>
                                <a class="navbar-item" :href="rootpath + 'pages/list.htm?list=author'">
                                    <span class="icon"><i class="fas fa-feather-alt"></i></span>
                                    <span>受賞者一覧</span>
                                </a>
                                <a class="navbar-item" :href="rootpath + 'pages/list.htm?list=book'">
                                    <span class="icon"><i class="fas fa-book"></i></span>
                                    <span>受賞作一覧</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </nav>
            </div>

            <div class="hero-body has-text-centered has-background-dark">
                <div class="container">
                    <h1 class="title has-text-light">{{ title }}</h1>
                    <h2 class="subtitle is-6 has-text-light">{{ subtitle }}</h2>
                </div>
            </div>
        </header>
    `
});