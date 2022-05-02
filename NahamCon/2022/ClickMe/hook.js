Java.perform(function(){
    Java.use("com.example.clickme.MainActivity").getFlagButtonClick.implementation = function (a) {
      console.log(this.getFlag());
      return;
    }
});