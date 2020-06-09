<template>
  <div>
    <banner></banner>
    <b-container fluid class="gallery-container">
      <div class="row">
        <div
          class="col-xs-12 col-sm-12 col-md-4 offset-md-8 col-lg-4 offset-lg-8 col-xl-4 offset-xl-8 col align-self-end"
        >
          <upload></upload>
        </div>
      </div>

      <div class="gallery-view">
        <div class="row">
          <div class="col-xs-12 col-sm-12 col-md-3 col-lg-3">
            <h5 class="date">JUNE 2020</h5>
          </div>
          <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
            <hr class="divider" />
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

export default {
  name: "gallery",
  data() {
    return {
      persistedGoogleCreds:""
    }
  },
  created() {
    this.persisLoginCreds();

  },

  methods: {
    persisLoginCreds() {
      this.$root.$on('creds came till here', googleCreds => {
        this.persistedGoogleCreds = googleCreds;
        console.log("WAIT WHAT", this.persistedGoogleCreds);
      })
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
</style>


