/** ページ情報 */
let pages = {
    home:         {no:0, text:"HOME", url:"index.htm"},
    awardList:   {no:1, text:"文学賞一覧", url:"pages/list.htm?list=award"},
    bookList:    {no:2, text:"受賞作一覧", url:"pages/list.htm?list=book"},
    authorList:  {no:3, text:"受賞者一覧", url:"pages/list.htm?list=author"}
}

/**
 * ページ情報を取得する
 * @param {*} rootpath 
 * @param {*} key 
 */
function getPageInfo(rootpath, key) {
    if (key in pages) {
        return {
            no: pages[key]["no"],
            text: pages[key]["text"],
            url: rootpath + pages[key]["url"]
        };
    } else {
        return {
            no: "999",
            text: key,
            url: "#"
        };
    }
}

/**
 * リクエストパラメータ（GET）を取得する
 * @returns HashMap形式のデータ
 */
function getRequestParams() {
    let query = location.search;
    let q = query.substring(1);
    let values = q.split("&");
    let params = {};
    for (let value of values) {
        let v = value.split("=");
        params[v[0]] = v[1];
    }
    return params;
}

/**
 * HEADタグにTwitter card用のMETAタグを追加する
 * @param {*} url 
 * @param {*} title 
 * @param {*} description 
 * @param {*} image 
 */
function addTwitterCardMetaTags(url, title, description, image) {
    document.querySelector("meta[property='og:url']").setAttribute("content", url);
    document.querySelector("meta[property='og:title']").setAttribute("content", title);
    document.querySelector("meta[property='og:description']").setAttribute("content", description);
    document.querySelector("meta[property='og:image']").setAttribute("content", image);
}

/**
 * Elemntオブジェクトを作成する
 * @param {*} tag タグ名 
 * @param {*} attr 属性
 * @returns 
 */
function createElem(tag, attr) {
    var elem = document.createElement(tag);
    for (a of attr) {
        elem.setAttribute(a.key, a.value);
    }
    return elem;
}
