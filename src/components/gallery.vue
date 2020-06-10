<template>
  <div>
    <banner></banner>
    <b-container fluid class="gallery-container">
      <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-4 offset-md-10 col-lg-4 offset-lg-9 col-xl-4 offset-xl-9 col align-self-end">
            <button type="button" class="btn btn-info" @click="routeToEdit"><font-awesome-icon icon="plus"/> Add New Entry</button>
        </div>
      </div>

      <div class="gallery-view">
        <div class="row">
           <div class="col-xs-12 col-sm-12 col-md-3 col-lg-3">
            <h5>JUNE 2020</h5>
          </div>
        </div>
        <div class="row">
           <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
            <hr class="divider" />
          </div>
          <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6" >
            <img v-for="image in images" :src="image" :alt="image.alt" class="col-xs-12 col-sm-12 col-md-6 col-lg-6 image_class" />
          </div>
         
        </div>

        <div class="row">
          <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
            <!-- <div v-for="n in 100">
              <img v-bind:src="`../assets/photos/${n}.png`" />
            </div>-->
          </div>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
import banner from "./banner.vue";
import upload from "./upload.vue";
import getImageListURL from "../awsCalls/getImageListURL.js";
export default {
  name: "gallery",
  data() {
    return {
      images: []
    };
  },
  mounted() {},
  created: function() {
    this.images = getImageListURL("NickGulson", [
      "MikeGrad1.jpeg",
      "MikeGrad2.jpeg"
    ]);
    console.log(this.images);
  },
  methods: {
    routeToEdit() {
      this.$router.push({ name: "templatePage" });

    }


  },
  components: {
    banner,
    upload
  }
};
</script>

<style lang="scss" scoped>
.divider {
  box-shadow: inset 0 0 10px #000000;
}
.gallery-view {
  margin: 3em 0 0 0;
}

.image_class{
  width: 75%;
  height: 50%;
  background-position: 50% 50%;
  background-repeat: no-repeat;
  background-size: cover;
}

.btn-info {
  margin: 2em 0 0 0;
}
</style>


