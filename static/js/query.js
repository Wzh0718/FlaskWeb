function querybtn() {
    $("#query-btn").on('click',function (event){
        var $this = $(this)
        var idcard = $("input[name='idcard']").val();
        if(!idcard){
            alert('请输入身份证号')
            return
        }
        // var divstyle =document.getElementById("query_results")
        // divstyle.style='display:"" '
    })
}


$(function (){
    querybtn();
})