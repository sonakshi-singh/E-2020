<template>
  <div>
    <banner></banner>

    <div v-if="edit!=false">
      <edit v-bind:form="this.form"></edit>
      <div class="row">
        <div class="col-sm-12 col-md-6 offset-lg-3 col-lg-6 offset-lg-3">
          <div class="upload-wrapper">
            <upload></upload>
          </div>
        </div>
      </div>
      <button class="btn btn-primary" @click="submit">Submit</button>
    </div>
    <div v-if="edit!=true" class="view-container">
      <templateView></templateView>
      <!-- <div class="row">
        <div class="col-sm-12 col-md-6 col-lg-6">
      
        </div>
      </div> -->
      <!-- <button class="btn btn-primary" @click="back">Go Back!</button> -->
    </div>
  </div>
</template>
<script>
import banner from "./banner.vue";
import GoogleLogin from "vue-google-login";
import templateView from "./templateView.vue";
import upload from "./upload.vue";
import edit from "./edit.vue";
import getImageListURL from "../awsCalls/getImageListURL.js";
export default {
  name: "templatePage",
  data() {
    return {
      templateEmail: "",
      edit: true,
      form: {
        title: "",
        value: "",
        text1: "",
        text2: "",
        image1: "",
        image2: ""
      },
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
  created: function() {
    this.templateEmail = this.$route.params.goingToTemplate;
    console.log("templateEmail", this.templateEmail);
    var images = getImageListURL("NickGulson", [
      "nick_12.png",
      "nick_23.png"
    ]);
    this.form.image1 = images[0];
    this.form.image2 = images[1];
    console.log("now", this.form);
  },
  methods: {
    back() {
      this.edit = true;
    },
    submit() {
      this.edit = false;
      //console.log(this.edit)
    },
    onSuccess(googleUser) {
      console;
      console.log(googleUser);
      // This only gets the user information: id, name, imageUrl and email
      console.log(googleUser.getBasicProfile());
    },
    onFailure(error) {
      console.log(error);
      // This only gets the user information: id, name, imageUrl and email
      // console.log(googleUser.getBasicProfile());
    }
  },
  components: {
    banner,
    GoogleLogin,
    templateView,
    edit,
    upload
  }
};
</script>

<style lang="scss" scoped>
.btn-primary {
  background-color: #b3d9f2;
  color: black;
  margin: 2em 0 0 0;
}
.upload-wrapper {
    margin: -3em 0 0 0;
}
.view-container {
    height: 100%;
}
</style>
