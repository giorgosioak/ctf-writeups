Java.perform(function(){
    Java.use("com.example.captain_hook.MainActivity").onCreate.implementation = function (a) {
      console.log(this.stringFromJNI());
      return;
    }
});