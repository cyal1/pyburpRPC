console.log("Script loaded successfully ");
var instances_array = [];
function callEncryptfunction(msg) {
    var ret = null
    Java.perform(function () { 
        if (instances_array.length == 0) { // if array is empty
            // call no-static method
            Java.choose("com.example.www.lib_common.crypto.JniUtils", { // instance class
                onMatch: function (instance) {
                    console.log("Found instance: " + instance);
                    instances_array.push(instance);
                    var string_class = Java.use("java.lang.String");
                    // var my_string = string_class.$new(msg).getBytes();
                    // console.log(typeof msg)
                    ret = instance.b(string_class.$new(msg).getBytes());
                    console.log(ret);
                    // send(ret)
                    return
                },
                onComplete: function () {
                    if (instances_array.length == 0) {
                        console.log("Not found encrypt instance. " );
                    }
                }

            });
        }
        else {//else if the array has some values
            console.log("An instance already exists." );
            var string_class = Java.use("java.lang.String");
            // var my_string = string_class.$new(msg.message).getBytes();
            // ret = instances_array[0].b(string_class.$new(msg).getBytes());
            ret = instances_array[0].b(string_class.$new(msg));
            console.log(ret);
            // send(ret)
        }

    });

    return ret
}


function callStaticEncryptfunction(msg) {
    var ret = null
    Java.perform(function () { 
        // call static method
        var obj = Java.use("com.example.www.lib_common.crypto.JniUtils");
        var string_class = Java.use("java.lang.String");
        // var my_string = string_class.$new(msg).getBytes();
        // console.log(typeof msg)
        // ret = obj.b(string_class.$new(msg).getBytes());
        ret = obj.b(string_class.$new(msg));
    });

    return ret
}

function callStaticDecryptfunction(msg) {
    var ret = null
    Java.perform(function () { 
        // call static method
        var obj = Java.use("com.example.www.lib_common.crypto.JniUtils");
        var string_class = Java.use("java.lang.String");
        // var my_string = string_class.$new(msg).getBytes();
        // console.log(typeof msg)
        // ret = obj.a(string_class.$new(msg).getBytes());
        ret = obj.a(string_class.$new(msg));
    });

    return ret
}

// // 
// function hookEncrypt() { 
//     Java.perform(function () {
//         var my_class = Java.use("com.yuanrenxue.match2022.security.Sign");
//         var string_class = Java.use("java.lang.String");
//         my_class.encrypt.overload().implementation = function(){ // static method
//             var my_string = string_class.$new("TE ENGANNNNEEE");
//             return my_string;
//         }
//     });
// }

rpc.exports = {
    callencryptfunction: callStaticEncryptfunction,
    calldecryptfunction: callStaticDecryptfunction,
    // hookencryptfunction: hookEncrypt
};
