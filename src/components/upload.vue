<!--
<template >
  <div id="upload-container">
    <!-- <div style="background-image: url(./src/body.jpg);"> -->
    <!-- <img alt="Vue logo" src="./body.jpg">  
    <h1 style="font-size:60px;">Welcome to Bene</h1>
    <h2>Name:  </h2>
    <input  :value="this.username" placeholder ="username" @change="nameChange">
    <div class="testing">
      <h2>This was successful</h2>
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
export default {
  name: 'Upload',
  data(){
    return{
      file:[],
      test:true,
      username: "",
      imageName : "",
      file2:false
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
}

</script>

<style >
.ret{
    width: 300px;
    height :500px;
    padding:20px;
}

#upload-container { 
  /* background-image: url("./body.jpg");
  background-size: length; */
  /* background-color: darkslategray; */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color:black;
  margin-top: 60px;
}

</style>-->