<script>
  // let name = "leonardo"
	let promise = "";
	let nameArtist = ""
	async function getArtist(name) {
    // faz um request GET para endpoint /filmes
		const res = await fetch(`http://localhost:8000/artistas/${name}` );
		const text = await res.json();
		if (res.ok) { return text; } 
    else { throw new Error(text);}
	}
  function handleClick() {
		return promise = getArtist(nameArtist);
	}
</script>
<form action="">
  <input bind:value={nameArtist}>
  <button on:click={() => handleClick()}>artist</button>
</form>


{#await promise}
	<p>...waiting</p>
{:then artistas}
	<h1>Lista de Artista</h1>
		{#each artistas as artista}
			
		<!-- <p>{artista.name}</p> -->
			<p>id = {artista.id}</p>
			<p>name = {artista.name}</p>
			<p>biography = {artista.biography}</p>
			<img src="https://image.tmdb.org/t/p/w185{artista.image}" alt="">
		
		{/each}
        <!-- <img src="{artista.image}" alt=""> -->
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}
