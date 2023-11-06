<script>
    let promise = getFilmes();
    let searchTerm = "";
  
    async function getFilmes() {
      const res = await fetch(`http://localhost:8000/filmes`);
      const text = await res.json();
      if (res.ok) {
        return text;
      } else {
        throw new Error(text);
      }
    }
  
    function handleClick() {
      promise = getFilmes();
    }
  </script>
  
  <div class="title flexCenter">

      <div class="nome text-center">
        <h1>CapiMovies</h1>
      </div>

    <input type="text" bind:value={searchTerm} placeholder="Pesquisar filmes" />
    <button on:click={handleClick}><i class="bi bi-search"></i></button>
  </div>

  {#await promise}
  <p>...aguardando</p>
  {:then filmes}

  <div class="container bg-info">
    <h1>MELHORES FILMES</h1>
  </div>

  <div class="content flexCenter">
    {#each filmes as filme}
    <div class="movies">        
          <img src={filme.image} alt="capa" />
          <button class="icon"><i class="bi bi-heart"></i></button>
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
        width: calc(15% - 1rem); /* Calcula a largura de cada filme, com 1rem de margem */
        margin: 0.5rem; /* Adiciona uma margem de 0.5rem entre os filmes */
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
        background-color: #0d7df597; /* Cor de fundo do botão */
        color: #fff; /* Cor do texto do botão */
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #fcfcfc; /* Cor de fundo do botão ao passar o mouse */
    }

    h1 {
        font-size: 24px;
    }

</style>
