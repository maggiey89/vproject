<template>

<body>
    <section>
        <div class="form-box">
            <div class="form-value">
                <form action="">
                    <h2>Login</h2>
                    <div class="inputbox">
                        <ion-icon name="mail-outline"></ion-icon>
                        <input type="email" required>
                        <label for="">Email</label>
                    </div>
                    <div class="inputbox">
                        <ion-icon name="lock-closed-outline"></ion-icon>
                        <input type="password" required>
                        <label for="">Password</label>
                    </div>
                    <div class="forget">
                        <label for=""><input type="checkbox">Remember Me</label>
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
    

</body>

</template>

<script>

</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    font-family: 'poppins', 'sans-serif';
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
</style>