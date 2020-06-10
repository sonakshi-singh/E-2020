<template >
  <div id="upload-container">
    <!-- <div style="background-image: url(./src/body.jpg);"> -->
    <!-- <img alt="Vue logo" src="./body.jpg"> -->
    <GoogleLogin
      :params="params"
      :renderParams="renderParams"
      :onSuccess="onSuccess"
      :onFailure="onFailure"
    ></GoogleLogin>
    <GoogleLogin :params="params" :logoutButton="true">Logout</GoogleLogin>
    <h1 style="font-size:60px;">Welcome to Bene</h1>
    <h2>Name:</h2>
    <input :value="this.username" placeholder="username" @change="nameChange" />
    <div class="testing">
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text" id="inputGroupFileAddon01" @click="onUpload">Upload</span>
        </div>
        <div class="custom-file">
          <input
            type="file"
            class="custom-file-input"
            id="inputGroupFile01"
            aria-describedby="inputGroupFileAddon01"
            @change="onFileChanged"
          />
          <label class="custom-file-label" for="inputGroupFile01">Choose file</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios"
import getImageURL from "../awsCalls/getImageURL.js";
import GoogleLogin from "vue-google-login";

export default {
  name: "upload",
  data() {
    return {
      file: [],
      test: true,
      username: "",
      filename: "",
      imageName: "",
      file2: false,
      params: {
        client_id:
          "991176984652-n9j3cc8mk83kgc2tc6hn0i1ubcpt3qod.apps.googleusercontent.com"
      },
      // only needed if you want to render the button with the google ui
      renderParams: {
        width: 250,
        height: 50,
        longtitle: true
      }
    };
  },

  methods: {
    // generate_pdf(){
    //   const doc=new jspdf()
    //   doc.text("Fact Sheet Bitches",15,15)
    //   doc.save("Bene_Travel.pdf")
    // },

    onFileChanged(event) {
      this.file = event.target.files[0];
      console.log("fileboi", this.file);
    },

    nameChange(event) {
      this.username = event.target.value;
      this.username = this.filename;

      // console.log(this.file2)
    },
    onUpload() {
      // upload file
      // this.test=false
      var image = document.getElementById("uploaded");

      image.src = URL.createObjectURL(this.file);
      alert("This was succesful");
      //console.log("upload file")
      //console.log(this.test,"yo")
      // console.log("hehheeh")
      uploadImage(this.file, this.username);
      this.imageName = this.username + "/" + this.file.name;
      this.file2 = getImage(this.imageName);
    },
    //   onSuccess(googleUser) {
    //       console.log(googleUser);

    //       // This only gets the user information: id, name, imageUrl and email
    //       console.log(googleUser.getBasicProfile());
    //       var h=googleUser.getBasicProfile();
    //       this.filename=h.getEmail();
    //       console.log(h.getEmail());
    // >>>>>>> d6dacd2fca8b2a5ee2138c3449824b2949b1db5a
    //     },
    onFailure(error) {
      console.log(error);
    }
  },
  components: {
    GoogleLogin
  }
};
</script>

<style >
.ret {
  width: 300px;
  height: 500px;
  padding: 20px;
}

#upload-container {
  /* background-image: url("./body.jpg");
  background-size: length; */
  /* background-color: darkslategray; */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  margin-top: 60px;
}
</style>