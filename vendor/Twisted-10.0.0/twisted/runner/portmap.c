begin_unit
begin_comment
comment|/*  * Copyright (c) 2001-2004 Twisted Matrix Laboratories.  * See LICENSE for details.   *   */
end_comment
begin_comment
comment|/* portmap.c: A simple Python wrapper for pmap_set(3) and pmap_unset(3) */
end_comment
begin_include
include|#
directive|include
file|<Python.h>
end_include
begin_include
include|#
directive|include
file|<rpc/rpc.h>
end_include
begin_include
include|#
directive|include
file|<rpc/pmap_clnt.h>
end_include
begin_function
DECL|function|portmap_set
specifier|static
name|PyObject
modifier|*
name|portmap_set
parameter_list|(
name|PyObject
modifier|*
name|self
parameter_list|,
name|PyObject
modifier|*
name|args
parameter_list|)
block|{
name|unsigned
name|long
name|program
decl_stmt|,
name|version
decl_stmt|;
name|int
name|protocol
decl_stmt|;
name|unsigned
name|short
name|port
decl_stmt|;
if|if
condition|(
operator|!
name|PyArg_ParseTuple
argument_list|(
name|args
argument_list|,
literal|"llih:set"
argument_list|,
operator|&
name|program
argument_list|,
operator|&
name|version
argument_list|,
operator|&
name|protocol
argument_list|,
operator|&
name|port
argument_list|)
condition|)
return|return
name|NULL
return|;
name|pmap_unset
argument_list|(
name|program
argument_list|,
name|version
argument_list|)
expr_stmt|;
name|pmap_set
argument_list|(
name|program
argument_list|,
name|version
argument_list|,
name|protocol
argument_list|,
name|port
argument_list|)
expr_stmt|;
name|Py_INCREF
argument_list|(
name|Py_None
argument_list|)
expr_stmt|;
return|return
name|Py_None
return|;
block|}
end_function
begin_function
DECL|function|portmap_unset
specifier|static
name|PyObject
modifier|*
name|portmap_unset
parameter_list|(
name|PyObject
modifier|*
name|self
parameter_list|,
name|PyObject
modifier|*
name|args
parameter_list|)
block|{
name|unsigned
name|long
name|program
decl_stmt|,
name|version
decl_stmt|;
if|if
condition|(
operator|!
name|PyArg_ParseTuple
argument_list|(
name|args
argument_list|,
literal|"ll:unset"
argument_list|,
operator|&
name|program
argument_list|,
operator|&
name|version
argument_list|)
condition|)
return|return
name|NULL
return|;
name|pmap_unset
argument_list|(
name|program
argument_list|,
name|version
argument_list|)
expr_stmt|;
name|Py_INCREF
argument_list|(
name|Py_None
argument_list|)
expr_stmt|;
return|return
name|Py_None
return|;
block|}
end_function
begin_decl_stmt
DECL|variable|PortmapMethods
specifier|static
name|PyMethodDef
name|PortmapMethods
index|[]
init|=
block|{
block|{
literal|"set"
block|,
name|portmap_set
block|,
name|METH_VARARGS
block|,
literal|"Set an entry in the portmapper."
block|}
block|,
block|{
literal|"unset"
block|,
name|portmap_unset
block|,
name|METH_VARARGS
block|,
literal|"Unset an entry in the portmapper."
block|}
block|,
block|{
name|NULL
block|,
name|NULL
block|,
literal|0
block|,
name|NULL
block|}
block|}
decl_stmt|;
end_decl_stmt
begin_function
DECL|function|initportmap
name|void
name|initportmap
parameter_list|(
name|void
parameter_list|)
block|{
operator|(
name|void
operator|)
name|Py_InitModule
argument_list|(
literal|"portmap"
argument_list|,
name|PortmapMethods
argument_list|)
expr_stmt|;
block|}
end_function
end_unit
