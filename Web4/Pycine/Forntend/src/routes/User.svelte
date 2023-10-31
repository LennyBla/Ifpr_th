<script>
    import '../globals.css'
    let loginResposta = "";
    let signupResposta = "";

    async function sendForm(e, respostaVariavel) {
        e.preventDefault();
        // envia o formulario no formato json
        let formData = new FormData(e.target);
        let data = Object.fromEntries(formData.entries());
        const res = await fetch("http://localhost:8000/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        const json = await res.json();
        respostaVariavel = JSON.stringify(json);
        e.target.reset();
    }
</script>

<div class="container">
    <p>{loginResposta}</p>

    <form class="crud-left" on:submit|preventDefault={() => sendForm(event, 'loginResposta')}>
        <div class="left-login">
            <div class="card-login">
             <h1>Login</h1>

            <div class="textfield">
                <label for="usuario">Usuario</label>
                <input type="text" name="username" placeholder="Username" required autocomplete="off"/>
            </div>

            <div class="textfield">
                <label for="senha">Senha</label>
                <input type="password" name="password" placeholder="Password" required autocomplete="off"/>
            </div>

                <button type="submit" class="btn-login">Login</button>
            </div>
        </div>
    </form>
</div>
<div class="container">
    <p>{signupResposta}</p>

    <form class="crud-right" on:submit|preventDefault={() => sendForm(event, 'signupResposta')}>
        <div class="right-login">
            <div class="card-cadastro">
                 <h1>Cadastre-se</h1> 
    
                <div class="textfield">
                    <label for="Nome completo">Nome completo</label>
                    <input type="text" name="name"placeholder="Nome" required autocomplete="off"/>
                </div>

                <div class="textfield">
                    <label for="email">Email</label>
                    <input type="text" name="email"  placeholder="Email" required autocomplete="off"/>
                </div>

                <div class="textfield">
                    <label for="senha">Senha</label>
                    <input type="password" name="password" placeholder="Password" required autocomplete="off"/>
                </div>  

                <div class="textfield">
                    <label for="senha">Confirmação de Senha</label>
                    <input type="password" name="password" placeholder="Password" required autocomplete="off"/>
                </div> 

                <button type="submit" class="btn-login">cadastrar</button>
            </div>
        </div>
    </form>
</div>
<style>
    .container {
        width: 100vw;
        height: 100vh;
        background: #000000be;
        display: flex;
        justify-content: center;
        align-items: center ;
    }
    
    .left-login{
        width: 50vw;
        height: 100vh;
        display: flex;
        justify-content: left;
        align-items: left;
        flex-direction: column;
    }
    .right-login{
        width: 50vw;
        height: 100vh;
        display: flex;
        justify-content: right;
        align-items: right;
    }
  
    .card-login{
        width: 90%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 50px 35px;
        background: #000000;
        border-radius: 20px;
        box-shadow: 0px 10px 10px #373737;
    }
    .card-login > h1{
        color: #00ff88;
        font-weight: 800;
        margin: 0%;
    } 
    .card-cadastro {
        width: 90%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 50px 35px;
        background: #00000084;
        border-radius: 20px;
        box-shadow: 0px 10px 10px #000000;
    }
    .card-cadastro > h1{
        font-size: 3vw;
        color:#77ffc0;
    }  

    .crud-left {
        width: 50vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .card-login >h1 {
        font-size: 3vw;
        color:#77ffc0;
    }
    
    .crud-right {
        width: 50vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .textfield{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        margin: 10px 0px;
    }
    .textfield > input{
        width: 100%;
        border: none;
        border-radius: 10px;
        padding: 15px;
        background: #343434;
        color:#f0ffffde;
        font-size: 12pt;
        box-shadow: 0px 10px 10px #000000;
        outline: none;
        box-sizing: border-box;
    }
    .textfield > label{
        color: #f0ffffde;
        margin-bottom: 10px;
    }
    .textfield > input::placeholder {
        color: #f0ffff94;
    }
    .btn-login{
        width: 50%;
        padding: 16px 0px;
        margin:5%;
        border: none;
        border-radius:8px ;
        outline: none;
        text-transform: uppercase;
        font-weight: 300;
        letter-spacing: 3px;
        color: #2b134b;
        background: #00ff88;
        cursor: pointer;
        box-shadow: 0px 10px 20px -12px #00ff8052;
    }

</style>
