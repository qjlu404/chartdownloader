//========================================================================
//
// StdinPDFDocBuilder.h
//
// This file is licensed under the GPLv2 or later
//
// Copyright 2010 Hib Eris <hib@hiberis.nl>
// Copyright 2010, 2018 Albert Astals Cid <aacid@kde.org>
//
//========================================================================

#ifndef STDINPDFDOCBUILDER_H
#define STDINPDFDOCBUILDER_H

#include "PDFDocBuilder.h"

//------------------------------------------------------------------------
// StdinPDFDocBuilder
//
// The StdinPDFDocBuilder implements a PDFDocBuilder that read from stdin.
//------------------------------------------------------------------------

class StdinPDFDocBuilder : public PDFDocBuilder
{

public:
    PDFDoc *buildPDFDoc(const GooString &uri, GooString *ownerPassword = nullptr, GooString *userPassword = nullptr, void *guiDataA = nullptr) override;
    bool supports(const GooString &uri) override;
};

#endif /* STDINPDFDOCBUILDER_H */
