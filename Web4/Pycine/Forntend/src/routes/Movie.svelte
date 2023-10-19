<script>
    let promise = getFilmes();
    let searchTerm = ""; // Variável para armazenar o termo de pesquisa

    async function getFilmes() {
        // Faz uma solicitação GET para endpoint /filmes com o termo de pesquisa
        const res = await fetch(`http://localhost:8000/filmes?search=${searchTerm}`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    export function handleClick() {
        promise = getFilmes();
    }
</script>

<div class="title flexCenter">
    <h1>Filmes</h1>
    <input type="text" bind:value={searchTerm} placeholder="Pesquisar filmes" />
    <button on:click={handleClick}>Pesquisar</button>
</div>
{#await promise}
    <p>...aguardando</p>
{:then filmes}
    <div class="content flexCenter">
        {#each filmes as filme}
            <div class="movies boxBorder">
                <p>{filme.title}</p>
                <img src={filme.image} alt="capa" />
                <button>Favoritar</button>
            </div>
        {/each}
    </div>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}


<style>
    .content {
		display: flex;
    	flex-wrap: wrap;
    	justify-content: space-between;
    }
    .movies{
        text-align: center;
    }
	.title {
    display: flex;
    flex-direction: column;
    align-items: center;
	}
    button{ 
        margin: .3rem auto;
        display: block;
    }
    .title {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        margin-bottom: 20px;
    }

    input[type="text"] {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        margin-right: 10px;
        font-size: 16px;
        width: 600px;
    }

    button {
        padding: 10px 20px;
        background-color: #007BFF; /* Cor de fundo do botão */
        color: #fff; /* Cor do texto do botão */
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #0056b3; /* Cor de fundo do botão ao passar o mouse */
    }

    h1 {
        font-size: 24px;
    }

</style>