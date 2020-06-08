<template>
  <b-navbar class="navbar">
    <b-navbar-brand class="bene-logo">
      <router-link :to="'/'">
        <img src="../assets/logo-white.png" />
        <span class="typewriter">
          <!-- <span class="typewriter-text">Be Well</span> -->
        </span>
      </router-link>
    </b-navbar-brand>
  </b-navbar>
</template>

<script>
export default {
  name: "banner",
  data() {
    return {};
  }
};
</script>

<style lang="scss" scoped>
.navbar {
  background-color: red;
  height: 6em !important;

  .bene-logo {
    padding-bottom: 0.5em;
    a {
      display: flex;
      align-items: center;
    }
  }

  img {
    height: 60%;
    width: 50%;
  }

  .typewriter {
    font-family: Courier, monospace;
    margin: 1em 0 0 0;
  }

  .typewriter-text {
    display: inline-block;
    overflow: hidden;
    letter-spacing: 2px;
    animation: typing 2s steps(60, end), blink 0.75s step-end infinite;
    white-space: nowrap;
    font-size: 18px;
    font-weight: 400;
    color: white;
    // border-right: 4px solid orange;
    box-sizing: border-box;
  }

  @keyframes typing {
    from {
      width: 0%;
    }
    to {
      width: 100%;
    }
  }

  @keyframes blink {
    from,
    to {
      border-color: transparent;
    }
    50% {
      border-color: orange;
    }
  }
}

/* DEMO-SPECIFIC STYLES */

::selection {
  background: black;
}
@media only screen and (min-device-width: 768px) and (max-device-width: 1400px) {
  img {
    position: relative;
    // margin-left: -80px !important; /* 50% of your logo width */
    display: block;
    // height: 60%;
    // width: 50%;
  }

    .typewriter-text {
    display: inline-block;
    overflow: hidden;
    letter-spacing: 2px;
    animation: typing 2s steps(60, end), blink 0.75s step-end infinite;
    white-space: nowrap;
    font-size: 15px;
    font-weight: 400;
    color: white;
    // border-right: 4px solid orange;
    box-sizing: border-box;
  }
}
</style>
