<template>
  <div>
    <b-container fluid class="template-container">
      <div class="row">
        <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
          <div class="form-group">
            <input :value="this.title" class="title form-control" placeholder="Title" type="text" />
          </div>
        </div>
      </div>

      <div class="row mx-auto">
        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
          <img :src="this.images[0]" class="mem-images" />
        </div>
        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 mx-auto">
          <div class="form-group memory-box">
            <label for="exampleFormControlTextarea1">Your favorite memory</label>
            <textarea
              :value="this.messages[0]"
              class="txt form-control"
              id="exampleFormControlTextarea1"
              @change="messageChange"
              rows="3"
            ></textarea>
            <!-- <input  placeholder="text"  /> -->
          </div>
        </div>
      </div>
      <div class="row mx-auto">
        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 mx-auto">
          <input :value="this.messages[1]" class="txt" placeholder="text" />
        </div>
        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 mx-auto">
          <img :src="this.images[1]" class="mem-images" />
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
<<<<<<< HEAD
export default {
  name: "template",
  data() {
    return {
      title: "title",
      images: [],
      messages: []
    };
  },
  methods: {
    messageChange(event) {
      console.log(event);
      console.log(this.images);
    }
  },
  components: {},
  created: function() {
    this.images = [
      "https://beneimages.s3.us-east-2.amazonaws.com/NickGulson/MikeGrad1.jpeg",
      "https://beneimages.s3.us-east-2.amazonaws.com/NickGulson/MikeGrad2.jpeg"
    ];
    console.log(this.images);
=======
import getImageListURL from "../awsCalls/getImageListURL.js"
export default {
    name:"template",
    data(){
        return {
            title: "title",
            images: [],
            messages: []
        }
    },
    methods: {
      messageChange(event){
        console.log(event)
        console.log(this.images)
      }
    },
    components: {
    },
    created: function() {
      this.images = getImageListURL("NickGulson", ["MikeGrad1.jpeg","MikeGrad2.jpeg"])
      console.log(this.images)
>>>>>>> 10701ffc7343f9694866e95fbf29fb3301746dfc
  }
};
</script>

<style lang="scss" scoped>
.template-container {
  // position: relative;
  text-align: center;
  padding-top: 5%;
  background-image: url("../assets/grad.jpg");
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  background-size: cover;
  min-height: 100%;
}

.txt {
  width: 200px;
  height: 300px;
}
.mem-images {
  max-width: 100px;
  // max-height: 100px;
  // height: auto;
  
  position:absolute;

  // height: auto;
  // width: 300px;
  // height: 400px;
  // padding: 20px;
}


/***** TITLE STYLING *****/
input[type="text"],
select.form-control {
  background: transparent;
  border: none;
  border-bottom: 1px solid #000000;
  -webkit-box-shadow: none;
  box-shadow: none;
  border-radius: 0;
}

input[type="text"]:focus,
select.form-control:focus {
  -webkit-box-shadow: none;
  box-shadow: none;
}
</style>