import { MeshReflectorMaterial } from '@react-three/drei'
import { Physics, usePlane } from '@react-three/cannon'
import { Guy } from './components/Guy'
import { Chair, Table, Lamp } from './components/Furniture'
import { XRCanvas, Hands, Controllers } from '@coconut-xr/natuerlich/defaults'
import { NonImmersiveCamera, useEnterXR, ImmersiveSessionOrigin, SessionModeGuard, VisibilitySessionModeGuard } from '@coconut-xr/natuerlich/react'

const sessionOptions = {
  requiredFeatures: ["local-floor"],
  optionalFeatures: ["hand-tracking"],
};


export default function App() {
  const enterAR = useEnterXR('immersive-ar', sessionOptions)

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        display: 'flex',
        flexDirection: 'column'
      }}>
      <button onClick={enterAR}>Enter AR</button>
      <XRCanvas dpr={[1, 2]} shadows>
        <NonImmersiveCamera rotation={[-Math.PI / 5, -Math.PI / 4, 0, 'YZX']} position={[-40, 50, 40]} fov={25} near={1} far={100} />
        <SessionModeGuard deny="immersive-ar">
          <fog attach="fog" args={['#171720', 60, 100]} />
        </SessionModeGuard>
        <ambientLight intensity={0.2} />
        <pointLight position={[-20, -5, -20]} color="red" />
        <Physics allowSleep={false} iterations={15} gravity={[0, -200, 0]}>
          <Guy rotation={[-Math.PI / 3, 0, 0]} />
          <Floor position={[0, 0, 0]} rotation={[-Math.PI / 2, 0, 0]} />
          <Chair position={[0, 0, -2.52]} />
          <Table position={[8, 0, 0]} />
          <Lamp position={[0, 25, 0]} />
        </Physics>
        <ImmersiveSessionOrigin scale={10}>
          <Hands type="grab" />
          <Controllers type="grab" />
        </ImmersiveSessionOrigin>
      </XRCanvas>
    </div>
  )
}

function Floor(props) {
  const [ref] = usePlane(() => ({ type: 'Static', ...props }))
  return (
    <VisibilitySessionModeGuard deny="immersive-ar">
      <mesh ref={ref} receiveShadow>
        <planeGeometry args={[100, 100]} />
        <meshPhongMaterial />
      </mesh>
    </VisibilitySessionModeGuard>
  )
}