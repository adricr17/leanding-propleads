import React from 'react';
import {Composition} from 'remotion';
import {Prueba} from './Prueba';
import {Susto} from './susto/Susto';
import {DURACION, FPS} from './susto/edicion';
import {NovatoPro} from './novatopro/NovatoPro';
import {DURACION as DUR_NP} from './novatopro/guion';
import {Minuto, duracionTotal} from './minuto/Minuto';
import {EPISODIOS} from './minuto/episodios';

// Proyecto vertical de PHARAON: 1080x1920 a 30 fps.
export const Root: React.FC = () => (
  <>
    <Composition id="Prueba" component={Prueba} width={1080} height={1920} fps={30} durationInFrames={60} />
    <Composition id="SustoSiz0" component={Susto} width={1080} height={1920} fps={FPS} durationInFrames={DURACION} />
    <Composition id="NovatoProDM" component={NovatoPro} width={1080} height={1920} fps={30} durationInFrames={DUR_NP} />
    {EPISODIOS.map((ep) => (
      <Composition key={ep.id} id={`Minuto-${ep.id.replace('_', '-')}`} component={Minuto} width={1080} height={1920} fps={30}
        durationInFrames={duracionTotal(ep)} defaultProps={{ep}} />
    ))}
  </>
);
