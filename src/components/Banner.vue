<template>
  <b-navbar class="navbar">
    <b-navbar-brand>
      <img src="../assets/logo-white.png" />
    </b-navbar-brand>
  </b-navbar>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {};
  }
};
</script>

<style lang="scss" scoped>
.navbar {
  background-color: red;
  height: 8em !important;
  img {
    // position: absolute;
    // left: 40%;
    // margin-left: -80px !important; /* 50% of your logo width */
    // display: block;
    height: 80%;
    width: 70%;
    margin-left: -5em;
  }
}

@media only screen and (min-device-width: 768px) and (max-device-width: 1400px) {
  img {
    position: absolute;
    left: 40%;
    margin-left: -80px !important; /* 50% of your logo width */
    display: block;
    height: 80%;
    width: 70%;
  }
}
</style>