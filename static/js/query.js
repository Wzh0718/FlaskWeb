function check() {
    const inputElement = document.getElementById("idcard");
    console.log(inputElement)
    if (inputElement.value === ""){
        alert("请输入身份证进行查询");
        return false;
    }
    return true;
}