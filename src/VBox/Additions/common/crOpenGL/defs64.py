# Copyright (c) 2001, Stanford University
# All rights reserved.
#
# See the file LICENSE.txt for information on redistributing this software.

import sys

import apiutil

apiutil.CopyrightDef()

print "LIBRARY VBoxOGL"
print "DESCRIPTION \"\""
print "EXPORTS"

# XXX can't these values be automatically computed by analyzing parameters?

exports_special = [
  'Accum',
  'AlphaFunc',
  'AreTexturesResident',
  'ArrayElement',
  'Begin',
  'BindTexture',
  'Bitmap',
  'BlendFunc',
  'CallList',
  'CallLists',
  'Clear',
  'ClearAccum',
  'ClearColor',
  'ClearDepth',
  'ClearIndex',
  'ClearStencil',
  'ClipPlane',
  'Color3b',
  'Color3bv',
  'Color3d',
  'Color3dv',
  'Color3f',
  'Color3fv',
  'Color3i',
  'Color3iv',
  'Color3s',
  'Color3sv',
  'Color3ub',
  'Color3ubv',
  'Color3ui',
  'Color3uiv',
  'Color3us',
  'Color3usv',
  'Color4b',
  'Color4bv',
  'Color4d',
  'Color4dv',
  'Color4f',
  'Color4fv',
  'Color4i',
  'Color4iv',
  'Color4s',
  'Color4sv',
  'Color4ub',
  'Color4ubv',
  'Color4ui',
  'Color4uiv',
  'Color4us',
  'Color4usv',
  'ColorMask',
  'ColorMaterial',
  'ColorPointer',
  'CopyPixels',
  'CopyTexImage1D',
  'CopyTexImage2D',
  'CopyTexSubImage1D',
  'CopyTexSubImage2D',
  'CullFace',
  'DebugEntry',
  'DeleteLists',
  'DeleteTextures',
  'DepthFunc',
  'DepthMask',
  'DepthRange',
  'Disable',
  'DisableClientState',
  'DrawArrays',
  'DrawBuffer',
  'DrawElements',
  'DrawPixels',
  'EdgeFlag',
  'EdgeFlagPointer',
  'EdgeFlagv',
  'Enable',
  'EnableClientState',
  'End',
  'EndList',
  'EvalCoord1d',
  'EvalCoord1dv',
  'EvalCoord1f',
  'EvalCoord1fv',
  'EvalCoord2d',
  'EvalCoord2dv',
  'EvalCoord2f',
  'EvalCoord2fv',
  'EvalMesh1',
  'EvalMesh2',
  'EvalPoint1',
  'EvalPoint2',
  'FeedbackBuffer',
  'Finish',
  'Flush',
  'Fogf',
  'Fogfv',
  'Fogi',
  'Fogiv',
  'FrontFace',
  'Frustum',
  'GenLists',
  'GenTextures',
  'GetBooleanv',
  'GetClipPlane',
  'GetDoublev',
  'GetError',
  'GetFloatv',
  'GetIntegerv',
  'GetLightfv',
  'GetLightiv',
  'GetMapdv',
  'GetMapfv',
  'GetMapiv',
  'GetMaterialfv',
  'GetMaterialiv',
  'GetPixelMapfv',
  'GetPixelMapuiv',
  'GetPixelMapusv',
  'GetPointerv',
  'GetPolygonStipple',
  'GetString',
  'GetTexEnvfv',
  'GetTexEnviv',
  'GetTexGendv',
  'GetTexGenfv',
  'GetTexGeniv',
  'GetTexImage',
  'GetTexLevelParameterfv',
  'GetTexLevelParameteriv',
  'GetTexParameterfv',
  'GetTexParameteriv',
  'Hint',
  'IndexMask',
  'IndexPointer',
  'Indexd',
  'Indexdv',
  'Indexf',
  'Indexfv',
  'Indexi',
  'Indexiv',
  'Indexs',
  'Indexsv',
  'Indexub',
  'Indexubv',
  'InitNames',
  'InterleavedArrays',
  'IsEnabled',
  'IsList',
  'IsTexture',
  'LightModelf',
  'LightModelfv',
  'LightModeli',
  'LightModeliv',
  'Lightf',
  'Lightfv',
  'Lighti',
  'Lightiv',
  'LineStipple',
  'LineWidth',
  'ListBase',
  'LoadIdentity',
  'LoadMatrixd',
  'LoadMatrixf',
  'LoadName',
  'LogicOp',
  'Map1d',
  'Map1f',
  'Map2d',
  'Map2f',
  'MapGrid1d',
  'MapGrid1f',
  'MapGrid2d',
  'MapGrid2f',
  'Materialf',
  'Materialfv',
  'Materiali',
  'Materialiv',
  'MatrixMode',
  'MultMatrixd',
  'MultMatrixf',
  'NewList',
  'Normal3b',
  'Normal3bv',
  'Normal3d',
  'Normal3dv',
  'Normal3f',
  'Normal3fv',
  'Normal3i',
  'Normal3iv',
  'Normal3s',
  'Normal3sv',
  'NormalPointer',
  'Ortho',
  'PassThrough',
  'PixelMapfv',
  'PixelMapuiv',
  'PixelMapusv',
  'PixelStoref',
  'PixelStorei',
  'PixelTransferf',
  'PixelTransferi',
  'PixelZoom',
  'PointSize',
  'PolygonMode',
  'PolygonOffset',
  'PolygonStipple',
  'PopAttrib',
  'PopClientAttrib',
  'PopMatrix',
  'PopName',
  'PrioritizeTextures',
  'PushAttrib',
  'PushClientAttrib',
  'PushMatrix',
  'PushName',
  'RasterPos2d',
  'RasterPos2dv',
  'RasterPos2f',
  'RasterPos2fv',
  'RasterPos2i',
  'RasterPos2iv',
  'RasterPos2s',
  'RasterPos2sv',
  'RasterPos3d',
  'RasterPos3dv',
  'RasterPos3f',
  'RasterPos3fv',
  'RasterPos3i',
  'RasterPos3iv',
  'RasterPos3s',
  'RasterPos3sv',
  'RasterPos4d',
  'RasterPos4dv',
  'RasterPos4f',
  'RasterPos4fv',
  'RasterPos4i',
  'RasterPos4iv',
  'RasterPos4s',
  'RasterPos4sv',
  'ReadBuffer',
  'ReadPixels',
  'Rectd',
  'Rectdv',
  'Rectf',
  'Rectfv',
  'Recti',
  'Rectiv',
  'Rects',
  'Rectsv',
  'RenderMode',
  'Rotated',
  'Rotatef',
  'Scaled',
  'Scalef',
  'Scissor',
  'SelectBuffer',
  'ShadeModel',
  'StencilFunc',
  'StencilMask',
  'StencilOp',
  'TexCoord1d',
  'TexCoord1dv',
  'TexCoord1f',
  'TexCoord1fv',
  'TexCoord1i',
  'TexCoord1iv',
  'TexCoord1s',
  'TexCoord1sv',
  'TexCoord2d',
  'TexCoord2dv',
  'TexCoord2f',
  'TexCoord2fv',
  'TexCoord2i',
  'TexCoord2iv',
  'TexCoord2s',
  'TexCoord2sv',
  'TexCoord3d',
  'TexCoord3dv',
  'TexCoord3f',
  'TexCoord3fv',
  'TexCoord3i',
  'TexCoord3iv',
  'TexCoord3s',
  'TexCoord3sv',
  'TexCoord4d',
  'TexCoord4dv',
  'TexCoord4f',
  'TexCoord4fv',
  'TexCoord4i',
  'TexCoord4iv',
  'TexCoord4s',
  'TexCoord4sv',
  'TexCoordPointer',
  'TexEnvf',
  'TexEnvfv',
  'TexEnvi',
  'TexEnviv',
  'TexGend',
  'TexGendv',
  'TexGenf',
  'TexGenfv',
  'TexGeni',
  'TexGeniv',
  'TexImage1D',
  'TexImage2D',
  'TexImage3D',
  'TexParameterf',
  'TexParameterfv',
  'TexParameteri',
  'TexParameteriv',
  'TexSubImage1D',
  'TexSubImage2D',
  'Translated',
  'Translatef',
  'Vertex2d',
  'Vertex2dv',
  'Vertex2f',
  'Vertex2fv',
  'Vertex2i',
  'Vertex2iv',
  'Vertex2s',
  'Vertex2sv',
  'Vertex3d',
  'Vertex3dv',
  'Vertex3f',
  'Vertex3fv',
  'Vertex3i',
  'Vertex3iv',
  'Vertex3s',
  'Vertex3sv',
  'Vertex4d',
  'Vertex4dv',
  'Vertex4f',
  'Vertex4fv',
  'Vertex4i',
  'Vertex4iv',
  'Vertex4s',
  'Vertex4sv',
  'VertexPointer',
  'Viewport',
  'wglChoosePixelFormat',
  'wglCopyContext',
  'wglCreateContext',
  'wglCreateLayerContext',
  'wglDeleteContext',
  'wglDescribeLayerPlane',
  'wglDescribePixelFormat',
  'wglGetCurrentContext',
  'wglGetCurrentDC',
  'wglGetDefaultProcAddress',
  'wglGetLayerPaletteEntries',
  'wglGetPixelFormat',
  'wglGetProcAddress',
  'wglMakeCurrent',
  'wglRealizeLayerPalette',
  'wglSetLayerPaletteEntries',
  'wglSetPixelFormat',
  'wglShareLists',
  'wglSwapBuffers',
  'wglSwapLayerBuffers',
  'wglSwapMultipleBuffers',
  'wglUseFontBitmapsA',
  'wglUseFontBitmapsW',
  'wglUseFontOutlinesA',
  'wglUseFontOutlinesW',
  'wglChoosePixelFormatEXT',
  'wglGetPixelFormatAttribivEXT',
  'wglGetPixelFormatAttribfvEXT',
  'wglGetExtensionsStringEXT',
  'CopyContext',
  'CreateContext',
  'CreateLayerContext',
  'DeleteContext',
  'DescribeLayerPlane',
  'DescribePixelFormat',
  'GetLayerPaletteEntries',
  'GetProcAddress',
  'RealizeLayerPalette',
  'ReleaseContext',
  'SetContext',
  'SetLayerPaletteEntries',
  'SetPixelFormat',
  'ShareLists',
  'SwapBuffers',
  'SwapLayerBuffers',
  'ValidateVersion',
]

noexport_special = [
    "BoundsInfoCR",
    "CreateContext",
    "DestroyContext",
    "MakeCurrent",
    "WindowCreate",
    "WindowDestroy",
    "WindowSize",
    "WindowPosition",
    "WindowVisibleRegion",
    "WindowShow",
    "SwapBuffers"
]

keys = apiutil.GetDispatchedFunctions(sys.argv[1]+"/APIspec.txt")

for func_name in keys:
    if func_name in noexport_special:
        continue
    if func_name in exports_special:
        print "gl%s = cr_gl%s" % (func_name,func_name)

for func_name in ( "wglChoosePixelFormat", 
           "wglCopyContext",
           "wglCreateContext",
           "wglCreateLayerContext",
           "wglDeleteContext",
           "wglDescribeLayerPlane",
           "wglDescribePixelFormat",
           "wglGetCurrentContext",
           "wglGetCurrentDC",
           "wglGetLayerPaletteEntries",
           "wglGetPixelFormat",
           "wglGetProcAddress",
           "wglMakeCurrent",
           "wglRealizeLayerPalette",
           "wglSetLayerPaletteEntries",
           "wglSetPixelFormat",
           "wglShareLists",
           "wglSwapBuffers",
           "wglSwapLayerBuffers",
           "wglSwapMultipleBuffers",
           "wglUseFontBitmapsA",
           "wglUseFontBitmapsW",
           "wglUseFontOutlinesA",
           "wglUseFontOutlinesW", 
           "wglChoosePixelFormatEXT",
           "wglGetPixelFormatAttribivEXT",
           "wglGetPixelFormatAttribfvEXT",
           "wglGetExtensionsStringEXT"):
    print "%s = %s_prox" % (func_name,func_name)

print """DrvCopyContext
DrvCreateContext
DrvCreateLayerContext
DrvDeleteContext
DrvDescribeLayerPlane
DrvDescribePixelFormat
DrvGetLayerPaletteEntries
DrvGetProcAddress = wglGetProcAddress_prox
DrvRealizeLayerPalette
DrvSetLayerPaletteEntries
DrvShareLists
DrvSwapBuffers
DrvSwapLayerBuffers
DrvReleaseContext = DrvReleaseContext
DrvSetContext = DrvSetContext
DrvValidateVersion = DrvValidateVersion
DrvSetPixelFormat = DrvSetPixelFormat"""

print """crCreateContext
crMakeCurrent
crSwapBuffers
crGetProcAddress
VBoxCreateContext
VBoxGetWindowId
VBoxFlushToHost"""
#print "DllMain"