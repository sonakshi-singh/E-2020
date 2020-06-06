<template >
  <div>
    <!-- <div style="background-image: url(./src/body.jpg);"> -->
    <!-- <img alt="Vue logo" src="./body.jpg"> -->
    <h1 style="font-size:60px;">Welcome to Bene</h1>
    <h2>Name:  </h2>
    <input  :value="this.username" placeholder ="username" @change="nameChange">
    <div class="testing">
      <h2>This was successful</h2>
      <div id="sharing">
      <facebook id="icon" :url="url" scale="3"></facebook>
        <twitter :url="url" title="Check me on Github" scale="3"></twitter>
        <linkedin :url="url" scale="3"></linkedin>
        <telegram :url="url" scale="3"></telegram>
        <whats-app :url="url" title="Hello" scale="3"></whats-app>
        <pinterest :url="url" scale="3"></pinterest>
        <reddit :url="url" scale="3" title="My Github"></reddit>
        <google :url="url" scale="3"></google>
        <email :url="url" subject="Hello" scale="3"></email>
      </div>
      <br/>
      <input type="file" @change="onFileChanged">
      <button @click="onUpload">Upload!</button>  
      </div>
      <div v-if ='test!=false' >
        <img class="ret" id="uploaded" src="https://benetravel.s3.us-east-2.amazonaws.com/efc44718b9d1b7d960366a3bfa89f5c5.jpg">
      </div>
      <div v-if ='test!=true'>
        <img class="ret" src= this.file2 >
      </div>
    </div>
</template>

<script>
// import axios from "axios"
import uploadImage from "../awsCalls/uploadImage.js"
import getImage from "../awsCalls/getImage.js"
import {
  Facebook,
  Twitter,
  Linkedin,
  Pinterest,
  Reddit,
  Telegram,
  WhatsApp,
  Email,
  Google
} from "vue-socialmedia-share";
// import VueSocialSharing from 'vue-social-sharing'

// Vue.use(VueSocialSharing);
// var SocialSharing = require('vue-social-sharing');
// Vue.use(SocialSharing);

export default {
  name: 'share',
  data(){
    return{
      file:[],
      test:true,
      username: "",
      imageName : "",
      file2:false,
      url:"https://github.com/AakashKhuranaNU"
    }   
  },
  
  methods :{
    // generate_pdf(){
    //   const doc=new jspdf()  
    //   doc.text("Fact Sheet Bitches",15,15)
    //   doc.save("Bene_Travel.pdf")
    // },
    onFileChanged (event) {
    this.file = event.target.files[0]
    console.log(this.file)
    
  },
  nameChange(event){
    this.username = event.target.value
   // console.log(this.file2)

  },
  onUpload() {
    // upload file
    // this.test=false
    var image = document.getElementById('uploaded');
    
	image.src = URL.createObjectURL(this.file);   
    alert("This was succesful")
    //console.log("upload file")
    //console.log(this.test,"yo")
    // console.log("hehheeh")
    uploadImage(this.file,this.username)
    this.imageName = this.username + "/" + this.file.name
    this.file2 = getImage(this.imageName)
  }
    
    },
    components: {
    Facebook,
    Twitter,
    Linkedin,
    Pinterest,
    Reddit,
    Telegram,
    WhatsApp,
    Email,
    Google
  }
}

</script>

<style >
.ret{
    width: 300px;
    height :500px;
    padding:20px;
}

#sharing > span {
  padding: 1em;
}



/* #upload-container { 
  /* background-image: url("./body.jpg");
  background-size: length; */
  /* background-color: darkslategray; 
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color:black;
  margin-top: 60px;
} */

</style>