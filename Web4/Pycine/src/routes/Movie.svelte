<script>
	
	let promise = getFilmes();
	async function getFilmes() {
    // faz um request GET para endpoint /filmes
		const res = await fetch(`http://localhost:8000/filmes`);
		const text = await res.json();
		if (res.ok) { return text; } 
    else { throw new Error(text);}
	}
	function handleClick() {
		promise = getFilmes();
	}
</script>

<button on:click={handleClick}> Get filmes </button>

{#await promise}
	<p>...waiting</p>
{:then filmes}
	<h1>Lista de Filmes</h1>
    {#each filmes as filme}
        <p>{filme.title}</p>
        <img src="{filme.image}" alt="">
    {/each}
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}