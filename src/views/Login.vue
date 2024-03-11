<template>
  <section>
    <div class="form-box">
      <div class="form-value">
        <form action="">
          <h2>Login</h2>
          <div class="inputbox">
            <ion-icon name="mail-outline"></ion-icon>
            <input type="email" required />
            <label for="">Email</label>
          </div>
          <div class="inputbox">
            <ion-icon name="lock-closed-outline"></ion-icon>
            <input type="password" required />
            <label for="">Password</label>
          </div>
          <div class="forget">
            <label for=""><input type="checkbox" />Remember Me</label>
            <a href="#">Forget password</a>
          </div>
          <button>Log in</button>
          <div class="register">
            <p>Don't have an account<a href="#">Register</a></p>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "LoginPage",
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  font-family: "poppins", "sans-serif";
}

section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100%;
  background-color: rgb(141, 141, 163);
}

.form-box {
  position: relative;
  width: 400px;
  height: 450px;
  background-color: rgb(102, 142, 147);
  display: flex;
  justify-content: center;
  align-items: center;
}

h2 {
  font-size: 2em;
  color: white;
  text-align: center;
}

.inputbox {
  position: relative;
  margin: 30px 0;
  width: 350px;
  border-bottom: 2px solid white;
}

.inputbox label {
  position: absolute;
  top: -10px;
  left: 5px;
  font-size: 1em;
  color: white;
  pointer-events: none;
  transition: top 0.3s ease, font-size 0.3s ease;
}

input:focus ~ label,
input:focus ~ :valid {
  top: -25px;
  font-size: 1em;
}

.inputbox input {
  width: 100%;
  height: 50px;
  background-color: transparent;
  border: none;
  outline: none;
  font-size: 1em;
  padding: 0 35px 0 5px;
  color: white;
}

.inputbox ion-icon {
  position: absolute;
  right: 8px;
  color: white;
  font-size: 1.2em;
  top: 20px;
}

.forget {
  margin: -15px 0 15px;
  font-size: 1em;
  color: white;
  display: flex;
  align-items: center;
}
</style>
