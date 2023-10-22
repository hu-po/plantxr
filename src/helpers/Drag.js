import { createRef, useCallback, useEffect, useMemo, useRef } from 'react'
import { usePointToPointConstraint, useSphere } from '@react-three/cannon'

function useDragConstraint(child) {
  const cursor = useMemo(() => createRef(), [])
  const [, sphereApi] = useSphere(() => ({ collisionFilterMask: 0, type: 'Kinematic', mass: 0, args: [0.5] }), cursor)
  const isDown = useRef(false)
  const [, , api] = usePointToPointConstraint(cursor, child, { pivotA: [0, 0, 0], pivotB: [0, 0, 0] })
  useEffect(() => void api.disable(), [])
  const end = useCallback((e) => {
    isDown.current = false
    e.target.releasePointerCapture(e.pointerId)
    api.disable()
  }, [])
  const start = useCallback((e) => {
    isDown.current = true
    e.stopPropagation()
    e.target.setPointerCapture(e.pointerId)
    api.enable()
  }, [])

  const move = useCallback((e) => {
    if (!isDown.current) {
      return
    }
    sphereApi.position.set(e.point.x, e.point.y, e.point.z)
  }, [])
  return { onPointerLeave: end, onPointerUp: end, onPointerDown: start, onPointerMove: move }
}

export { useDragConstraint }