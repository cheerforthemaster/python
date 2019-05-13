function getUpload(){
    //alert("图片数据上传成功！");
    //window.location.href="http://localhost/analyze";

    var formData = new FormData();
    formData.append('file', $('#file')[0].files[0]);
    $.ajax({
        url: "/upload",
        type: "POST",
        dataType: "text",
        data: formData,
        processData: false,
        contentType: false,
        error: erryFunction,  //错误执行方法
        success: succFunction //成功执行方法
        })
        function erryFunction(data)
        {
            alert(data);
        }
        function succFunction(data)
        {
            //alert(data);
            sessionStorage["par1"]=data
            window.location.href="/analyze";
        }
}


