
Java.perform(function(){
  var ShowFlag = Java.use("com.example.slapapp.ShowFlag");
  var MainActivity = Java.use("com.example.slapapp.MainActivity");
  
  Java.use("com.example.slapapp.MainActivity").onCreate.implementation = function (bundle) {
    this.counter.value = 999999999;
    let ret = this.onCreate(bundle);
    return ret;
  }

  Java.use("android.os.Handler").postDelayed.overload('java.lang.Runnable', 'long').implementation = function (func,time) {
    let ret = this.postDelayed(func,1);
    return ret;
  }

  Java.use("com.example.slapapp.ShowFlag").onCreate.implementation = function (bundle) {
    console.log(this.stringFromJNI())
    let ret = this.onCreate(bundle);
    return ret;
  }
});