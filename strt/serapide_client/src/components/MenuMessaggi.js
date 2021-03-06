/*
 * Copyright 2018, GeoSolutions Sas.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
import React from 'react'
import {
    UncontrolledDropdown,
    DropdownToggle,
    DropdownMenu} from 'reactstrap'
import LinkWithIcon from './LinkWithIcon'

export default ({disabled, messaggi= []}) => (
    <UncontrolledDropdown tag="li" className="first menumessaggi text-white" inNavbar>
        <DropdownToggle tag="span">
            <LinkWithIcon className="vertical-divider-right" icon="email" iconColor="text-warning" withBadge badge={messaggi.length} label="Messaggi"></LinkWithIcon>
        </DropdownToggle>
        <DropdownMenu right className="shadow">
            {messaggi.map(({id, data, from, testo})=> (
                    <div key={id} className="d-flex message-item">
                        <i className="material-icons text-warning">fiber_manual_record</i>
                        <span className="d-inline-flex flex-column">
                                <span className="text-nowrap">{from.nome}</span>
                                <span className="text-nowrap text-uppercase">{from.organizzazione}</span>
                                <span className="py-2">{testo}</span>
                        </span>
                    </div>
            ))}
            {messaggi.length=== 0 ? (<span>Nessun messaggio</span>) : (<a href="#/messaggi/" className="d-block pt-4 text-center">Vai a utti i messagi</a>)}
            
        </DropdownMenu>
    </UncontrolledDropdown>
)