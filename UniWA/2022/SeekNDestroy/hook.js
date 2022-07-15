Java.perform(function(){
    Java.use("com.example.seek_n_destroy.MainActivity").onCreate.implementation = function (a) {
      console.log(this.stringFromJNI());

      let ret = this.onCreate(a);
      return ret;
    }
});
