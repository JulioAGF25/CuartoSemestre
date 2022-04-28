import React from 'react'

const Formulario = () => {
    return (
        <div className='bg-pink-300 ml-10 rounded-md p-4'>
            <h1 className=' text-center'>Formulario</h1>
            <form className='container mx-2'>
                <div>
                    <label htmlFor="nombrePaciente">Nombre Paciente </label>
                    <input type="text" className=' block rounded-md' />
                </div>
                <div>
                    <label htmlFor="email">Correo </label>
                    <input type="email" className='block rounded-md' />
                </div>
                <div>
                    <label htmlFor="sintomas">Sintomas </label>
                    <input type="text" className='block rounded-md' />
                </div>
                <div>
                    <label htmlFor="date">Fecha </label>
                    <input type="date" name="date" id="date" className='block rounded-md' />
                </div>


            </form>
        </div>
    )
}

export default Formulario