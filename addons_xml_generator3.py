# *
# * Copyright (C) 2012-2013 Garrett Brown
# * Copyright (C) 2010 j48antialias
# *
# * Este Programa é um software livre; você pode redistribuí-lo e / ou modificar
# * sob os termos da GNU General Public License conforme publicada por
# * a Free Software Foundation; tanto a versão 2, ou (por sua opção)
# * qualquer versão posterior.
# *
# * Este programa é distribuído na esperança de que seja útil,
# * mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
# * COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
# * GNU General Public License para obter mais detalhes.
# *
# * Você deve ter recebido uma cópia da GNU General Public License
# * junto com o XBMC; veja o arquivo COPYING. Se não, escreva para
# * the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# * http://www.gnu.org/copyleft/gpl.html
# *
# * Baseado no código de j48antialias:
# * https://anarchintosh-projects.googlecode.com/files/addons_xml_generator.py
 
"" "gerador addons.xml" ""
 
importar  os
import  sys
 
# Compatibilidade com 3.0, 3.1 e 3.2 não suportando literais u ""
se  sys . versão  <  '3' :
    importar  codecs
    def  u ( x ):
        retornar  codecs . unicode_escape_decode ( x ) [ 0 ]
mais :
    def  u ( x ):
        retornar  x
 
classe  Generator :
    "" "
        Gera um novo arquivo addons.xml a partir de cada arquivo addon.xml addons
        e um novo arquivo hash addons.xml.md5. Deve ser executado a partir da raiz de
        o repositório com check-out. Só lida com estrutura de pasta de profundidade única.
    "" "
    def  __init__ ( self ):
        # gerar arquivos
        eu . _generate_addons_file ()
        eu . _generate_md5_file ()
        # notificar usuário
        print ( "Atualização de arquivos xml e md5 de complementos concluída" )
 
    def  _generate_addons_file ( self ):
        # lista de complementos
        addons  =  os . listdir ( "." )
        # texto final de addons
        addons_xml  =  u ( "<? xml version = \" 1.0 \ " encoding = \" UTF-8 \ " standalone = \" yes \ " ?> \ n <addons> \ n " )
        # loop thru e adicionar cada arquivo addon.xml addons
        para  addon  em  addons :
            tente :
                # ignorar qualquer arquivo ou pasta .svn ou pasta .git
                if ( not  os . path . isdir ( addon ) ou  addon  ==  ".svn"  ou  addon  ==  ".git" ): continue
                # criar caminho
                _path  =  os . caminho . juntar ( addon , "addon.xml" )
                # linhas de divisão para decapagem
                xml_lines  =  open ( _path , "r" ). leia (). linhas de divisão ()
                # novo addon
                addon_xml  =  ""
                # loop através da limpeza de cada linha
                para  linha  em  xml_lines :
                    # pular linha de formato de codificação
                    if ( line . find ( "<? xml" ) > =  0 ): continue
                    # adicionar linha
                    se  sys . versão  <  '3' :
                        addon_xml  + =  unicode ( line . rstrip () +  " \ n " , "UTF-8" )
                    mais :
                        addon_xml  + =  linha . rstrip () +  " \ n "
                # conseguimos, então adicione ao nosso texto addons.xml final
                addons_xml  + =  addon_xml . rstrip () +  " \ n \ n "
            exceto  exceção  como  e :
                # addon.xml ausente ou mal formatado
                print ( "Excluindo% s para% s"  % ( _path , e ))
        # limpar e adicionar tag de fechamento
        addons_xml  =  addons_xml . strip () +  u ( " \ n </addons> \ n " )
        # salvar Arquivo
        eu . _save_file ( addons_xml . encode ( "UTF-8" ), arquivo = "addons.xml" )
 
    def  _generate_md5_file ( self ):
        # criar um novo hash md5
        tente :
            importar  md5
            m  =  md5 . novo ( open ( "addons.xml" , "r" ). read ()). hexdigest ()
        exceto  ImportError :
            importar  hashlib
            m  =  hashlib . md5 ( open ( "addons.xml" , "r" , encoding = "UTF-8" ). read (). encode ( "UTF-8" )). hexdigest ()
 
        # salvar Arquivo
        tente :
            eu . _save_file ( m . encode ( "UTF-8" ), arquivo = "addons.xml.md5" )
        exceto  exceção  como  e :
            # ops
            print ( "Ocorreu um erro ao criar o arquivo addons.xml.md5! \ n % s"  %  e )
 
    def  _save_file ( self , data , file ):
        tente :
            # grava dados no arquivo (use b para Python 3)
            abrir ( arquivo , "wb" ). escrever ( dados )
        exceto  exceção  como  e :
            # ops
            print ( "Ocorreu um erro ao salvar% s arquivo! \ n % s"  % ( arquivo , e ))
 
 
if ( __name__  ==  "__main__" ):
    # começar
    Gerador ()